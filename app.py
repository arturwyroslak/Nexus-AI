import streamlit as st
import time
from nexus.core import NexusOrchestrator, Agent, AgentConfig

st.set_page_config(page_title="Nexus-AI Orchestrator", page_icon="🧠", layout="wide")

st.title("🧠 Nexus-AI Orchestrator")
st.markdown("### Local Swarm Intelligence Control Plane")

# Sidebar Configuration
st.sidebar.header("Swarm Configuration")
swarm_mode = st.sidebar.selectbox("Swarm Mode", ["Research Team", "Dev Team", "Creative Team"])

# Initialize session state for orchestrator
if 'orchestrator' not in st.session_state:
    st.session_state.orchestrator = NexusOrchestrator()
    
    # Initialize default agents
    researcher = Agent(AgentConfig(name="Researcher", role="Data Gatherer", system_prompt="You find facts."))
    writer = Agent(AgentConfig(name="Writer", role="Content Creator", system_prompt="You write summaries."))
    reviewer = Agent(AgentConfig(name="Reviewer", role="Quality Control", system_prompt="You critique."))
    
    st.session_state.orchestrator.register_agent(researcher)
    st.session_state.orchestrator.register_agent(writer)
    st.session_state.orchestrator.register_agent(reviewer)

# Main Interface
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Mission Control")
    task_input = st.text_area("Define Task/Mission", "Analyze the trends in Generative AI for 2026.")
    
    if st.button("🚀 Launch Swarm", type="primary"):
        with st.spinner("Swarm is mobilizing..."):
            # Simulation of swarm activity
            results = st.session_state.orchestrator.run_swarm(task_input)
            time.sleep(1) # UX pause
            
            st.success("Mission Complete!")
            
            for res in results:
                st.info(res)

with col2:
    st.subheader("Live System Logs")
    log_container = st.empty()
    logs = st.session_state.orchestrator.logs
    st.code("\n".join(logs[-10:]), language="text")

st.markdown("---")
st.caption("Powered by Nexus-AI Protocol v0.1 | Running Locally")
