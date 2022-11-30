import pytest
from pathlib import Path
import yaml
import shutil
import subprocess

class Problem:
    def __init__(self, root):
        self.root = Path(root)
        self.name = self.root.name
        self._info = None

    @property
    def yaml_path(self):
        return self.root / "problem.yml"

    @property
    def d(self):
        return self.get_info()

    def get_info(self):
        if self._info is None:
            path = self.root / "problem.yml"
            self._info = yaml.safe_load(path.open())
        return self._info

    def get_path(self, filename):
        return self.root.joinpath(filename)

    def get_solution_path(self):
        return self.root.joinpath("solution", self.d['filename'])

    def run_tests(self, test_root):
        workdir = test_root / "work"
        shutil.copytree(self.root , workdir)

        for f in self.d['files']['solution']:
            shutil.copy(self.get_path(f), workdir)

        # if "prepare_script" in self.d:
        #     subprocess.run(f"cd {workdir} && python {self.d['prepare_script']}", shell=True, check=True)
        p = subprocess.run(f"cd {workdir} && py.test -v", shell=True)
        return p.returncode == 0

problems = [str(p.parent) for p in Path("problems").rglob("problem.yml")]

@pytest.mark.parametrize("problem_dir", problems)
def test_validate_problem_yaml(problem_dir):
    p = Problem(problem_dir)
    info = p.get_info()
    assert 'title' in info, "title missing in problem.yml"
    assert 'blurb' in info, "blurb missing in problem.yml"
    assert 'files' in info, "files missing in problem.yml"
    assert isinstance(info['files'], dict), "The value field of files must be a dict"

    for section in ['code', 'test', 'solution']:
        assert section in info['files'], f"Missing entry for {section} in files field"
        files = info['files'][section]
        assert isinstance(files, list), f"files.{section} is expected to be of type list, but found {type(files)}"
        for f in files:
            assert p.get_path(f).exists(), f"missing file {f}"


@pytest.mark.parametrize("problem_dir", problems)
def test_validate_solution(problem_dir, tmp_path):
    p = Problem(problem_dir)
    assert p.run_tests(tmp_path), f"tests failed"
