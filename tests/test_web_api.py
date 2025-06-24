from web_api import compare_agents


def test_compare_agents():
    script = ["msg", "error", "msg"]
    result = compare_agents(script)
    assert result["static"]["turns"] == 3
    assert result["static"]["errors"] == 0
    assert result["dynamic"]["errors"] == 1
