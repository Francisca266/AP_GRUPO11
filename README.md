# Speech Recognition

Este repositório contém o código para treinar e avaliar um modelo Wav2Vec2 pré-treinado usando o Medical ASR Recording Dataset. O objetivo é melhorar o reconhecimento automático de voz (ASR) para datasets públicos.

## Tabela de Conteúdos

- [Visão Geral](#visão-geral)
- [Estrutura de Diretórios](#estrutura-de-diretórios)
- [Requisitos](#requisitos)
- [Execução](#execução)
- [Referências](#referências)

## Visão Geral

Este projeto envolve:

1. Preparação e transformação do conjunto de dados de áudios médicos.
2. Fine-tuning de um modelo Wav2Vec2 para melhorar o ASR em áudios médicos.
3. Avaliação do modelo em novos audios médicos.
4. Avaliação do modelo em áudios gravados localmente.
5. Comparação do modelo antes e após o processo de Fine-Tuning.

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
## Execução
Para executar o modelo, siga estas etapas simples:

1. Certifique-se de ter todas as dependências instaladas.
2. Abra o arquivo `model.ipynb` em um ambiente compatível com Jupyter Notebook.
3. Execute todas as células do notebook.


Para executar a interface gráfica, siga estas etapas:
1. Instalar Flask com ```pip install Flask ```.
2. Abrir um terminal ou prompt de comando.
3. Navegar até o diretório do projeto.
4. Executar o seguinte comando:
   ``` python3 app.py ```
5. **Importante:** Ao executar a interface gráfica, observe que não foi possível incluir os arquivos de áudio de teste no repositório devido a restrições de tamanho. É necessário fazer o download desses ficheiros de áudio de teste em https://www.kaggle.com/datasets/paultimothymooney/medical-speech-transcription-and-intent e salvá-los numa pasta chamada 'recordings' dentro do diretório app/static.


## Referências
- [Hugging Face](https://huggingface.co/facebook/wav2vec2-base-100h)
- [Hugging Face](https://huggingface.co/datasets/Hani89/medical_asr_recording_dataset)
- [Hugging Face Documentation](https://huggingface.co/docs)
