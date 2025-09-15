if (-Not (Test-Path ".venv")) {
    uv sync
    Write-Host "`nVirtual environment created and dependencies installed."
    Start-Sleep -Seconds 2
} else {
    & .\.venv\Scripts\Activate.ps1
}

python main.py

