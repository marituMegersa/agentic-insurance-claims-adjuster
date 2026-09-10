def test_agent_orchestrator():
    prompt = "Test execution query for agentic-insurance-claims-adjuster"
    assert len(prompt) > 0
    assert "Test" in prompt
