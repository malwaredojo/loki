# The Loki Framework

<p align="center">
  <a href="https://github.com/malwaredojo/loki">
    <img src="https://github.com/malwaredojo/loki/blob/main/imgs/loki-logo.png" alt="Loki Framework" width="218" height="218">
  </a>
</p>

### Automated Command-Line Identity Generation Tool for OSINT Investigators

**[Installation](#installation--usage) • [Features](#features) • [Contributions](#contributions--license) • [Future Goals](#future-goals)**

---

## What's Loki?
**Loki** is a tool designed to create sock puppet identities for OSINT (Open-Source Intelligence) investigators, private investigators, or anyone needing a fake online presence that cannot be traced back to their real identity. Setting up a sock puppet manually can be time-consuming and requires knowing where to source credible fake information. **Loki** automates this process, generating detailed identity profiles with ease.

Currently in its initial development phase, **Loki** provides essential details for sock puppet creation, such as names, contact information, and more. As of March 14, 2025, it also includes an AI-generated image from [This Person Does Not Exist](https://thispersondoesnotexist.com/). The framework is actively evolving, with new features being added to enhance its capabilities.

To learn about our plans for future development, see the [Future Goals](#future-goals) section.

---

## Screenshot
![Loki Screenshot](https://github.com/malwaredojo/loki/blob/main/imgs/loki-screenshot.png)

---

## Installation & Usage

### Prerequisites
- Python 3.6 or higher
- `pip` (Python package manager)
- `git` (for cloning the repository)

### Setup with Virtual Environment

1. **Clone the repository**:
   ```bash
   git clone https://github.com/malwaredojo/loki.git
   cd loki/
   ```

2. **Create and activate a virtual environment**:

   - **On Linux/macOS**:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

   - **On Windows**:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```

   After activation, your terminal prompt should show `(venv)`.

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Navigate to the Loki directory**:
   ```bash
   cd loki
   ```

5. **Run the script**:
   ```bash
   python loki.py  # Use 'sudo' only if required (e.g., for file permissions)
   ```

6. **To deactivate the virtual environment when done**:
   ```bash
   deactivate
   ```

---

## Example Commands

- **Generate a basic identity**:
  ```bash
  python loki.py -s -b
  ```

- **Generate a female identity with a picture**:
  ```bash
  python loki.py -sp -g female -b
  ```

- **Generate a male engineer from the US in JSON format**:
  ```bash
  python loki.py -s -g male -p "Engineer" -n US -f json -b
  ```

- Run `python loki.py -h` for a full list of options.

---

## Features
- **Detailed Identity Generation**: Creates comprehensive sock puppet profiles with personal, professional, and contact details.
- **AI-Generated Image**: Includes an optional profile picture from *This Person Does Not Exist* (via `-sp`).
- **Customizable Options**: Specify gender (`-g`), profession (`-p`), and nationality (`-n`).
- **Multiple Output Formats**: Save data as TXT, JSON, or CSV (`-f`).
- **Cross-Platform**: Designed to work on Linux, macOS, and Windows with minimal dependencies.

---

## Future Goals
Here are the planned enhancements for Loki:
- **Full Distribution Independence**: Ensure seamless operation across all major operating systems with no platform-specific dependencies.
- **Automated Social Media Account Creation**: Enable automatic creation of social media profiles (e.g., Facebook, Instagram, TikTok) using the generated identity.
- **Enhanced Gender Switch**: Refine gender-specific generation to align perfectly with user preferences.
- **Nationality-Based Generation**: Add support for generating identities tailored to specific nationalities.
- **Expanded Output Formats**: Already implemented (TXT, JSON, CSV); future enhancements may include additional formats like YAML.

---

## Contributions & License
You can contribute in the following ways:
- Report bugs or suggest improvements via GitHub Issues.
- Add new features or tools by submitting a pull request.
- Share feedback to enhance functionality.

**Loki** is licensed under the **GPL 3.0 License**.
