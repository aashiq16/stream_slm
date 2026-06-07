# test_model.py

from services.slm_service import ask_slm

print(
    ask_slm(
        "Explain revenue growth in one sentence."
    )
)