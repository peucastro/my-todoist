{
  description = "my-todoist development environment";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = {
    nixpkgs,
    flake-utils,
    ...
  }:
    flake-utils.lib.eachDefaultSystem (
      system: let
        pkgs = import nixpkgs {inherit system;};

        pythonEnv = pkgs.python313.withPackages (p:
          with p; [
            requests
            python-dotenv
            todoist-api-python
          ]);
      in {
        formatter = pkgs.alejandra;

        devShells.default = pkgs.mkShell {
          packages = [
            pythonEnv
            pkgs.python313
            pkgs.ruff
          ];
        };
      }
    );
}
