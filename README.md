# Junior - A Voice Assistant Application

## Overview
Junior is a voice assistant application built using Python. It employs a clean architecture approach, separating the application into distinct layers: core, infrastructure, and application. This design promotes modularity, maintainability, and testability of the codebase.

## Key Features
- **Voice Interaction**: Junior can listen to voice commands and respond accordingly.
- **Hotword Detection**: The application can detect specific "hotwords" (e.g., "Junior") to initiate a conversation.
- **Transcription**: Junior uses the Whisper speech recognition model to transcribe audio input.
- **Task Execution**: The application can execute various tasks based on user input, such as setting reminders, sending messages, or performing web searches.
- **Text-to-Speech**: Junior can synthesize speech using the Azure Cognitive Services or Google Cloud Text-to-Speech APIs.
- **OpenAI Integration**: The application can engage in natural language conversations using the OpenAI language model.

## Architecture
The project follows a clean architecture approach, with the following layers:

1. **Core**: Contains the domain models, services, and repositories. This layer encapsulates the business logic of the application.
2. **Infrastructure**: Handles the technical details, such as logging, startup, and UI.
3. **Application**: Includes the interactors that implement the use cases.

This separation of concerns promotes modularity, testability, and maintainability of the codebase.

## Roadmap
The current version of Junior provides a solid foundation for a voice assistant application. Future development plans include:

1. **Improved Hotword Detection**: Enhance the accuracy and robustness of the hotword detection mechanism.
2. **Task Management**: Improve the task execution capabilities, allowing users to create, manage, and track various tasks.
3. **Personalization**: Introduce user profiles and personalization features to tailor the assistant's behavior to individual preferences.
4. **Multi-Modal Interaction**: Expand the application to support additional input and output modalities, such as text, images, and gestures.
5. **Offline Capabilities Enhancement**: Investigate ways to enable the application to fully offline, reducing dependency on internet connectivity.
6. **Multilingual Support**: Extend the application to support multiple languages, catering to a diverse user base.

## Getting Started
To run the Junior voice assistant application, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/yacobalemneh/junior.git
   ```
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Set up the necessary API keys (e.g., Azure Cognitive Services, OpenAI) in the `.env` file.
4. Run the application:
   ```
   python main.py
   ```

Alternatively, you can use the provided Visual Studio Code launch configurations to run the application in "Watch Mode" or directly execute the `main.py` script.

## Contributing
We welcome contributions from the community to help improve and expand the capabilities of the Junior voice assistant. If you're interested in contributing, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Implement your changes and ensure they adhere to the project's coding standards and architectural principles.
4. Write tests to cover your changes.
5. Submit a pull request, describing the changes you've made and the problem they solve.

We'll review your contribution and provide feedback. Once approved, your changes will be merged into the main codebase.

## License
This project is licensed under the [MIT License](LICENSE).

## Acknowledgments
Junior was inspired by the growing demand for intelligent voice assistants and the advancements in natural language processing and speech recognition technologies. We'd like to acknowledge the open-source community and the developers of the libraries and frameworks used in this project, including:

- [Whisper](https://github.com/openai/whisper) for speech recognition
- [Azure Cognitive Services](https://azure.microsoft.com/en-us/products/cognitive-services/) and [Google Cloud Text-to-Speech](https://cloud.google.com/text-to-speech) for text-to-speech capabilities
- [OpenAI](https://openai.com/) for the language model integration
- [PyAudio](https://people.csail.mit.edu/hubert/pyaudio/) for audio processing
- [Speech Recognition](https://pypi.org/project/SpeechRecognition/) for speech recognition
- [Keyboard](https://pypi.org/project/keyboard/) for keyboard interaction
- [Pyperclip](https://pypi.org/project/pyperclip/) for clipboard interaction
- [Coloredlogs](https://pypi.org/project/coloredlogs/) for colored logging


