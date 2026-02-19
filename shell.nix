{pkgs ? import <nixpkgs> {}}:
pkgs.mkShell {
  packages = with pkgs; [
    python3
  ];
  shellHook = ''
    echo "Welcome to Python dev shell"
    python -v
  '';
}
