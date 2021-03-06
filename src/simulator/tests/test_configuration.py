from pathlib import Path

from src.simulator.configuration import parse_configuration


def test_configuration():
	conf = parse_configuration(Path("~/university/jump_model_exp/python_proj/sample_config.json").expanduser())
	assert conf
	conf.validate()
