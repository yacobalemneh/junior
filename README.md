# Junior

Junior is a voice assistant application built using Python. It uses a clean architecture approach, separating the application into distinct layers: core, infrastructure, and application. The core layer contains the business logic, infrastructure contains the technical details, and application contains the use cases.

## Project Structure

The project is structured as follows:

- core: Contains the domain models, services, and repositories.
- infrastructure: Contains the technical details such as logging, startup, and UI.
- application: Contains the interactors which implement the use cases.
- config: Contains the configuration files.
- main.py: The entry point of the application.

### Core

The core layer contains the business logic of the application. It is further divided into domain and data_source.

- domain: Contains the domain models and services.
- data_source: Contains the data models and repositories.

### Infrastructure

The infrastructure layer contains the technical details of the application. It is further divided into audio, interaction, logging, startup, and ui.

### Application

The application layer contains the interactors which implement the use cases of the application.

### Config

The config layer contains the configuration files for the application.

### Main

The main.py file is the entry point of the application. It sets up the application and starts the conversation.

## Running the Application

To run the application, you can use the provided configurations in the `.vscode/launch.json` file:

- "Python: Watch Mode": This configuration runs the `watcher.py` script which monitors the project directory and restarts the main script whenever a file changes.
- "Python: Main": This configuration runs the `main.py` script directly.

The default configuration is "Python: Watch Mode".

## Dependencies

The project has several dependencies, including:

- pyaudio: For audio processing.
- speech_recognition: For speech recognition.
- keyboard: For keyboard interaction.
- pyperclip: For clipboard interaction.
- coloredlogs: For colored logging.
- whisper: For transcription.

## Configuration

The application's behavior can be configured using the JSON files in the config directory. The `hotwords.json` file contains the hotwords that the application listens for, and the `responses.json` file contains the responses that the application can give.

## Logging

The application uses Python's built-in logging module for logging. The logging level can be configured using the `LOG_LEVEL` environment variable.

## Conclusion

Junior is a voice assistant application built using Python and a clean architecture approach. It separates concerns into distinct layers, making the code easier to understand and maintain.