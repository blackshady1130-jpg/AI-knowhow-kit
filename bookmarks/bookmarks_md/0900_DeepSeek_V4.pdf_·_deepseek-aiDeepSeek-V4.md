Title: DeepSeek_V4.pdf · deepseek-ai/DeepSeek-V4-Pro at main

URL Source: https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro/blob/main/DeepSeek_V4.pdf

Markdown Content:
*   Libraries
*   [Transformers](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro?library=transformers)
How to use deepseek-ai/DeepSeek-V4-Pro with Transformers:

# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("text-generation", model="deepseek-ai/DeepSeek-V4-Pro")
messages = [
    {"role": "user", "content": "Who are you?"},
]
pipe(messages)# Load model directly
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("deepseek-ai/DeepSeek-V4-Pro")
model = AutoModelForCausalLM.from_pretrained("deepseek-ai/DeepSeek-V4-Pro")
*   Inference

*   [HuggingChat](https://huggingface.co/chat/models/deepseek-ai/DeepSeek-V4-Pro)
*   Notebooks
*   [Google Colab](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro/colab)
*   [Kaggle](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro/kaggle)
*   Local Apps[](https://huggingface.co/settings/local-apps#local-apps "Set up your favorite local applications")
*   [vLLM](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro?local-app=vllm)
How to use deepseek-ai/DeepSeek-V4-Pro with vLLM:

##### Install from pip and serve model

# Install vLLM from pip:
pip install vllm
# Start the vLLM server:
vllm serve "deepseek-ai/DeepSeek-V4-Pro"
# Call the server using curl (OpenAI-compatible API):
curl -X POST "http://localhost:8000/v1/chat/completions" \
	-H "Content-Type: application/json" \
	--data '{
		"model": "deepseek-ai/DeepSeek-V4-Pro",
		"messages": [
			{
				"role": "user",
				"content": "What is the capital of France?"
			}
		]
	}'
##### Use Docker

docker model run hf.co/deepseek-ai/DeepSeek-V4-Pro
*   [SGLang](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro?local-app=sglang)
How to use deepseek-ai/DeepSeek-V4-Pro with SGLang:

##### Install from pip and serve model

# Install SGLang from pip:
pip install sglang
# Start the SGLang server:
python3 -m sglang.launch_server \
    --model-path "deepseek-ai/DeepSeek-V4-Pro" \
    --host 0.0.0.0 \
    --port 30000
# Call the server using curl (OpenAI-compatible API):
curl -X POST "http://localhost:30000/v1/chat/completions" \
	-H "Content-Type: application/json" \
	--data '{
		"model": "deepseek-ai/DeepSeek-V4-Pro",
		"messages": [
			{
				"role": "user",
				"content": "What is the capital of France?"
			}
		]
	}'
##### Use Docker images

docker run --gpus all \
    --shm-size 32g \
    -p 30000:30000 \
    -v ~/.cache/huggingface:/root/.cache/huggingface \
    --env "HF_TOKEN=<secret>" \
    --ipc=host \
    lmsysorg/sglang:latest \
    python3 -m sglang.launch_server \
        --model-path "deepseek-ai/DeepSeek-V4-Pro" \
        --host 0.0.0.0 \
        --port 30000
# Call the server using curl (OpenAI-compatible API):
curl -X POST "http://localhost:30000/v1/chat/completions" \
	-H "Content-Type: application/json" \
	--data '{
		"model": "deepseek-ai/DeepSeek-V4-Pro",
		"messages": [
			{
				"role": "user",
				"content": "What is the capital of France?"
			}
		]
	}'
*   [Docker Model Runner](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro?local-app=docker-model-runner)
How to use deepseek-ai/DeepSeek-V4-Pro with Docker Model Runner:

docker model run hf.co/deepseek-ai/DeepSeek-V4-Pro
