# LLM_finetuning
This repository contains a fine-tuned Large Language Model (LLM) designed to power a financial chatbot. The model has been fine-tuned on a domain-specific financial dataset containing question-answer pairs, enabling it to provide accurate and context-aware responses to a wide range of finance-related queries.


# Llama-3.2 Question Answering Fine-Tuning Project

## Prerequisites
- Python 3.8+
- PyTorch
- Transformers
- PEFT
- bitsandbytes
- Weights & Biases (wandb)

## Installation
```bash
pip install transformers peft bitsandbytes torch datasets wandb
```



## Hyperparameters
### Model Configuration
- **Model**: meta-llama/Llama-3.2-3B-Instruct
- **Quantization**: 4-bit with double quantization
  - Quantization Type: FP4
  - Compute Dtype: float16

### LoRA Configuration
- **Rank (r)**: 32
- **LoRA Alpha**: 32
- **Target Modules**: 
  - q_proj, o_proj, k_proj
  - down_proj, gate_proj, v_proj
- **Dropout**: 0.1
- **Bias**: None
- **Task Type**: Question Answering

### Training Arguments
- **Learning Rate**: 5e-5
- **Batch Size**: 
  - Train: 16 per device
  - Evaluation: 4 per device
- **Epochs**: 10
- **Gradient Accumulation Steps**: 4
- **Weight Decay**: 0.1
- **Optimization**: paged_adamw_8bit
- **Scheduler**: Linear
- **Early Stopping Patience**: 2 epochs

## Dataset Preparation
1. Prepare dataset with columns:
   - 'question'
   - 'context'
   - 'answer'

2. Use `preprocess_function` for tokenization
   - Max input length: 128 tokens
   - Padding: Maximum length
   - Truncation: Enabled

## Training Workflow
1. Load pre-trained Llama-3.2 model
2. Apply LoRA configuration
3. Tokenize dataset
4. Initialize Trainer
5. Start model training with W&B logging

## Monitoring
- Logging directory: `./logs`
- Weights & Biases tracking enabled
- Model checkpoints saved every 200 steps
- Maximum 3 checkpoints retained

## Notes
- Requires access to Llama-3.2 model
- GPU with sufficient memory recommended
- Wandb account needed for experiment tracking


## Loading the model
The model is too large in size for uploading on Github.
If you want load the model in your notebook, import it from HUGGING_FACE using
_model_name = "Akshit-77/llama-3.2-3b-chatbot"_

# Running the Interface
## Prerequisites

## Gradio
Jupyter Notebook
Trained model checkpoint

## Steps to Launch Interface

Open gradio_interface_with_RAG.ipynb
Ensure all dependencies are installed
Run notebook cells sequentially
Interface will launch in web browser

## Interface Usage

Input question in provided text box
Select context or input custom context
Click 'Generate' to get model response
Adjust parameters as needed

## Troubleshooting

Verify model path
Check CUDA/GPU availability
Confirm all dependencies installed
