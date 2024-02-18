# Code Shortcut Generator
The **Code Shortcut Generator** is a little tool built with PyQt5 that allows users to create custom shortcut snippets. With this tool, you can easily generate XML snippet files containing custom shortcuts and code snippets, which can then be imported into your favourite IDE.


## Getting Started
To use the **CodeShortcut Generator**, follow these steps:
  - **Download the Executable:** Download the executable file from the releases page of this repository.
  - **Run the Application:** Double-click on the executable file to run the app.
  - **Create Shortcuts:** Enter your desired shortcut's tile, shortcut and corresponding code in the respective input fields. Specify the language they're designed for. <br /> ![image](https://github.com/NRexha/CodeShortcutGenerator/assets/145846614/88b9c723-1925-4461-a7e1-5b2443f1c219)

    
- **Add Shortcut:** Click on the *Add Shortcut* button to add the shortcut and code snippet to the list on your right. You can add as many as you want.
 <br /> ![image](https://github.com/NRexha/CodeShortcutGenerator/assets/145846614/c7393541-9dd5-4add-ab52-1ca961987323)<br />

  - **Remove shortcut:** You can remove your shortcuts by clicking  on the *remove* button.
   <br /> ![image](https://github.com/NRexha/CodeShortcutGenerator/assets/145846614/6f99ddc8-325d-41c8-a319-d1f224e79890)<br />
      *Note: only the shortcuts present in the list will be exported*
  - **Change color:** You can change the color of your shortcuts by clicking on the *Change color* button.
    <br /> ![image](https://github.com/NRexha/CodeShortcutGenerator/assets/145846614/099397f7-a527-493c-9c18-3536b7e4af92)<br />
- **Export Snippets:** Once you have added all your shortcuts, click on the *Export* button to export the snippets to .snippet files.
  <br /> ![image](https://github.com/NRexha/CodeShortcutGenerator/assets/145846614/c292b791-efd5-4d3f-a66d-2001d6b52aa7)

## How to import snippet file and use it in Visual Studio
  - **Code Snippets Manager:** Go to the *Tools* menu, click on *Code Snippets Manager*
    <br /> ![image](https://github.com/NRexha/CodeShortcutGenerator/assets/145846614/ada0411f-10c6-4ad1-a277-78a69fd02d8c)<br />
  - **Select Language:** Choose the programming language for which you want to import the snippet file, in this case C#.
   <br /> ![image](https://github.com/NRexha/CodeShortcutGenerator/assets/145846614/9caa47d2-98ed-4c88-9c08-a92913d5589a)<br />
  - **Add File:** Click on the *Add...* button and navigate to the location of your snippet file and select it. You can choose any location (for isntance: MyCode Snippet)
   <br /> ![image](https://github.com/NRexha/CodeShortcutGenerator/assets/145846614/1f1271d7-d64c-48f2-84cc-5672f71fb937)<br />
  - **Import Snippet:** Click on the *Import* button to import the snippet file into Visual Studio.
  - **Use Snippet:** In your code editor, type the shortcut defined in your snippet file and press *Tab* to expand it into the corresponding code snippet. If the shortcut shows on your suggestions you can just press *Tab* twice and the code will be generated.

## Contributing
Im pretty new to code and tool development so there's a lot to improve for sure. If you encounter any issues or have any suggestions for improvements, please open an issue on GitHub.


