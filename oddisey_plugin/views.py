import os
import json
import subprocess
from pathlib import Path
from django.http import JsonResponse
from django.views import View


class AppInfoView(View):
    def get(self, request, *args, **kwargs):
        return JsonResponse(self.get_app_info())

    def get_app_info(self):
        return {
            "oddisey_version": self.get_package_version(),
            "openedx_version": self.get_git_info(),
            "pip_packages": self.get_installed_packages(),
        }

    def get_package_version(self):
        from . import __version__
        return __version__

    def get_git_info(self):
        try:
            repo_path = Path("/openedx/edx-platform/").resolve()
            branch = subprocess.check_output(
                ["git", "rev-parse", "--abbrev-ref", "HEAD"], cwd=repo_path
            ).strip().decode()

            sha = subprocess.check_output(
                ["git", "rev-parse", "HEAD"], cwd=repo_path
            ).strip().decode()

            commit_message = subprocess.check_output(
                ["git", "log", "-1", "--pretty=%B"], cwd=repo_path
            ).strip().decode()

            tag = subprocess.check_output(
                ["git", "describe", "--tags", "--exact-match"], cwd=repo_path
            ).strip().decode()

            return {"branch": branch, "commit_message": commit_message, "sha": sha, "tag": tag}
        except Exception:
            return "No Git Information Available"

    def get_installed_packages(self):
        try:
            pip_list = subprocess.check_output(["pip", "list", "--format", "json"])
            return json.loads(pip_list)
        except Exception:
            return "Could not retrieve installed packages"
