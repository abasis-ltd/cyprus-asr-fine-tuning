# 🗣️ Cypriot Greek ASR System

## 📅 Weekly Progress Breakdown

---

### Week 1: Initial Research and ASR Systems Comparison

**Overview**  
Week 1 focuses on setting up the development environment and comparing multiple ASR systems for Cypriot Greek dialect recognition.

**Key Activities**
- Installed and configured dependencies for various ASR APIs (Whisper, DeepGram, ElevenLabs, AssemblyAI, Speechmatics, Google Cloud)
- Created unified ModelPipeline class for testing different speech recognition systems
- Set up MLflow experiment tracking with ngrok for remote access
- Conducted baseline testing using Mozilla Common Voice Greek dataset
- Compared performance of open-source vs commercial ASR solutions

**Technologies Used**  
`faster-whisper`, `deepgram-sdk`, `elevenlabs`, `speechmatics-python`, `assemblyai`, `google-cloud-speech`, `torchaudio`, `librosa`, `datasets`, `mlflow`, `pyngrok`

---

### Week 2: Dataset Preparation and Cypriot Dictionary Development

**Overview**  
Week 2 focuses on creating and processing comprehensive datasets for Cypriot Greek dialect, including dictionary development and audio-text pair preparation.

**Key Activities**
- Developed comprehensive Cypriot Greek dictionary with 25,000+ word entries
- Created `DATASET_CLEARED.csv` with phonetic transcriptions and Greek translations
- Processed ABBYY dataset for additional language resources
- Built audio-text dataset pipelines for training data preparation
- Implemented data cleaning and standardization workflows

**Technologies Used**  
`pandas`, `numpy`, `csv processing`, `audio file handling`, `text preprocessing`, `data validation scripts`

---

### Week 3: Model Architecture Experiments and MLM Development

**Overview**  
Week 3 explores different model architectures and develops Masked Language Models specifically for Cypriot Greek dialect processing.

**Key Activities**
- Experimented with Wav2Vec2 architectures for Cypriot speech recognition
- Developed BERT-based MLM models for dialect-specific language understanding
- Conducted GPU vs CPU performance testing for model training
- Created prototype Cypriot BERT training pipeline
- Tested various model configurations and hyperparameters

**Technologies Used**  
`transformers`, `pytorch`, `wav2vec2`, `BERT architectures`, `GPU/CPU optimization`, `model training frameworks`

---

### Week 4: Model Fine-tuning and Optimization

**Overview**  
Week 4 focuses on fine-tuning pre-trained models specifically for Cypriot Greek dialect and optimizing model performance.

**Key Activities**
- Fine-tuned `lighteternal/wav2vec2-large-xlsr-53-greek` model for Cypriot dialect
- Fine-tuned `jonathas` Greek model with Cypriot dataset adaptations
- Implemented advanced training techniques with performance optimization
- Created model upload scripts for HuggingFace integration
- Conducted comprehensive model evaluation and comparison

**Technologies Used**  
`HuggingFace transformers`, `model fine-tuning frameworks`, `training optimization techniques`, `HuggingFace hub integration`

---

### Week 5: Model Testing and Performance Evaluation

**Overview**  
Week 5 focuses on comprehensive testing and evaluation of fine-tuned models to assess their performance on Cypriot Greek speech recognition.

**Key Activities**
- Conducted rigorous testing of Masked Language Models on Cypriot dialect
- Evaluated fine-tuned ASR models using multiple test datasets
- Performed detailed WER (Word Error Rate) analysis and performance metrics
- Compared model performance across different Cypriot speech samples
- Documented testing results and identified areas for improvement

**Technologies Used**  
`evaluation metrics`, `WER calculation`, `model testing frameworks`, `performance analysis tools`, `result visualization`

---

### Week 6: Final Integration and Language Model Enhancement

**Overview**  
Week 6 focuses on final model integration, combining multiple datasets, and implementing KENLM language models for enhanced Cypriot Greek speech recognition.

**Key Activities**
- Integrated multiple datasets for comprehensive model training
- Implemented KENLM n-gram language models for improved transcription accuracy
- Combined Brev datasets for enhanced training data coverage
- Conducted final model optimization and performance tuning
- Prepared production-ready models with complete evaluation pipelines

**Technologies Used**  
`KENLM`, `dataset integration`, `language model development`, `model optimization`, `production deployment preparation`

---

## ✅ Outcomes

Production-ready ASR system for **Cypriot Greek dialect** with:
- Integrated language models
- Comprehensive dataset coverage
- State-of-the-art performance metrics
