"""Module for LLM local configuration."""

from mlx_lm import load

MODEL_DEFAULT = "mlx-community/Llama-3.2-3B-Instruct-4bit"

model, tokenizer = load(MODEL_DEFAULT)
