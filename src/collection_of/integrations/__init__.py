from typing import List

from collection_of.integrations import (
    cargo_integration,
    conda_integration,
    dockerhub_integration,
    gitlab_integration,
    go_integration,
    maven_integration,
    npm_integration,
    pypi_integration,
)
from src.collection_of.integrations import collection_integration

# libio and github integrations are a bit special

AVAILABLE_PACKAGE_MANAGER: List[collection_integration.BaseIntegration] = [
    pypi_integration.PypiIntegration(),
    gitlab_integration.GitLabIntegration(),
    conda_integration.CondaIntegration(),
    npm_integration.NpmIntegration(),
    maven_integration.MavenIntegration(),
    dockerhub_integration.DockerhubIntegration(),
    cargo_integration.CargoIntegration(),
    go_integration.GoIntegration(),
]

# TODO: "helm_id", "brew_id", "apt_id", "yum_id", "snap_id", "dnf_id", "yay_id",
