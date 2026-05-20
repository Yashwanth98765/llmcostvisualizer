import streamlit as st
import pandas as pd
import plotly.express as px
import tiktoken

# --- 1. CONFIG & PRICING DATA ---
st.set_page_config(page_title="LLM Cost Visualizer", layout="wide")

# Pricing as of 2026 (USD per 1 Million Tokens)
# Feel free to update these as models change!
PRICING = {
    "GPT-4o-mini": {"input": 0.15, "output": 0.60},
    "GPT-4o": {"input": 2.50, "output": 10.00},
    "Claude 3.5 Sonnet": {"input": 3.00, "output": 15.00},
    "Claude Haiku 4.5": {"input": 1.00, "output": 5.00},
    "Gemini 1.5 Flash": {"input": 0.30, "output": 2.50}
}

# --- 2. HELPER FUNCTIONS ---
def count_tokens(text: str) -> int:
    """Counts tokens using OpenAI's cl100k_base encoding as a standard proxy."""
    if not text:
        return 0
    encoding = tiktoken.get_encoding("cl100k_base")
    return len(encoding.encode(text))

def calculate_costs(input_tokens: int, output_tokens: int) -> pd.DataFrame:
    """Calculates the cost for all models and returns a DataFrame."""
    data = []
    for model, rates in PRICING.items():
        input_cost = (input_tokens / 1_000_000) * rates["input"]
        output_cost = (output_tokens / 1_000_000) * rates["output"]
        total_cost = input_cost + output_cost
        
        data.append({
            "Model": model,
            "Input Cost ($)": input_cost,
            "Output Cost ($)": output_cost,
            "Total Cost ($)": total_cost
        })
    return pd.DataFrame(data)

# --- 3. UI LAYOUT ---
st.title(" LLM Token Cost Visualizer")
st.markdown("Estimate and compare API costs across popular Large Language Models.")

# Split into two columns: Inputs and Visualizations
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("1. Configure Prompts")
    
    input_text = st.text_area("Paste your Input Prompt here:", height=150)
    input_tokens = count_tokens(input_text)
    st.caption(f"**Calculated Input Tokens:** {input_tokens:,}")
    
    # We can't know exact output beforehand, so we let the user estimate it
    estimated_output_tokens = st.number_input(
        "Estimated Output Tokens (How long do you expect the response to be?)", 
        min_value=0, max_value=128000, value=500, step=100
    )
    
    # Add a multiplier to simulate high-volume API usage (e.g., processing 10,000 documents)
    api_calls = st.slider("Number of API Calls (Scale up!)", min_value=1, max_value=100000, value=1, step=100)

with col2:
    st.subheader("2. Cost Breakdown & Visualization")
    
    if input_tokens > 0 or estimated_output_tokens > 0:
        # Calculate base costs and apply multiplier
        df_costs = calculate_costs(input_tokens, estimated_output_tokens)
        df_costs["Input Cost ($)"] *= api_calls
        df_costs["Output Cost ($)"] *= api_calls
        df_costs["Total Cost ($)"] *= api_calls
        
        # Format for table display
        display_df = df_costs.copy()
        for col in ["Input Cost ($)", "Output Cost ($)", "Total Cost ($)"]:
            display_df[col] = display_df[col].apply(lambda x: f"${x:,.6f}")
        
        st.dataframe(display_df, use_container_width=True)
        
        # --- PLOTLY VISUALIZATION ---
        # Melt DataFrame for stacked bar chart
        df_melted = df_costs.melt(
            id_vars=["Model"], 
            value_vars=["Input Cost ($)", "Output Cost ($)"],
            var_name="Cost Type", 
            value_name="Cost"
        )
        
        fig = px.bar(
            df_melted, 
            x="Model", 
            y="Cost", 
            color="Cost Type", 
            title=f"Total Cost for {api_calls:,} API Calls",
            text_auto='.4f',
            color_discrete_sequence=["#636EFA", "#EF553B"]
        )
        fig.update_layout(xaxis_title="LLM Provider", yaxis_title="Cost (USD)", barmode='stack')
        
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("Enter some text or output tokens on the left to see the visualization.")