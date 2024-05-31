# Speech Recognition

Este repositório contém o código para treinar e avaliar um modelo Wav2Vec2 pré-treinado usando o Medical ASR Recording Dataset. O objetivo é melhorar o reconhecimento automático de voz (ASR) para audios médicos.

## Tabela de Conteúdos

- [Visão Geral](#visão-geral)
- [Estrutura de Diretórios](#estrutura-de-diretórios)
- [Requisitos](#requisitos)
- [Referências](#referências)

## Visão Geral

Este projeto envolve:

1. Preparação e transformação do conjunto de dados de audios médicos.
2. Treino de um modelo Wav2Vec2 para melhorar o ASR em audios médicos.
3. Avaliação do modelo em novos audios médicos.
4. Comparação do modelo antes e após o processo de Fine-Tuning.

## Estrutura de Diretórios

```plaintext

|
|__ /app                         # interface gráfica 
|   |__ templates
|   |__ app.py
|   |__ results_medical.csv
|   |__ /static
|       |__ /recordings          # audios dos dados de teste
|       |__ style.css
|__ model.ipynb                  # modelo
|__ record_audio.py              # gravação dos áudios de teste 





````

## Requisitos

As seguintes bibliotecas são fundamentais para a execução do código:

- Python >= 3.x
- Datasets
- Transformers
- PyTorch
- NumPy
- Matplotlib
- Evaluate

Para instalar as dependências é necessário executar o seguinte:

```bash
pip install datasets transformers torch numpy matplotlib evaluate
```


## Referências
- [Hugging Face](https://huggingface.co/facebook/wav2vec2-base-100h)
- [Hugging Face](https://huggingface.co/datasets/Hani89/medical_asr_recording_dataset)
- [PyTorch Documentation](https://pytorch.org/docs/stable/index.html)
- [Hugging Face Documentation](https://huggingface.co/docs)
