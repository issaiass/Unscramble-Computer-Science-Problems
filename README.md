<details open>
<summary> <b>Project Overview: Unscramble Computer Science Problems<b></summary>

In this project, we will complete five tasks based on a fabricated set of calls and texts exchanged during September 2016. We will use Python to analyze and answer questions about the texts and calls contained in the dataset. Lastly, we will perform run time analysis of your solution and determine its efficiency.


About the data:
- The text and call data are provided in csv files.
- The text data (text.csv) has the following columns: sending telephone number (string), receiving telephone number (string), timestamp of text message (string).
- The call data (call.csv) has the following columns: calling telephone number (string), receiving telephone number (string), start timestamp of telephone call (string), duration of telephone call in seconds (string)
- All telephone numbers are 10 or 11 numerical digits long. Each telephone number starts with a code indicating the location and/or type of the telephone number. There are three different kinds of telephone numbers, each with a different format:
- Fixed lines start with an area code enclosed in brackets. The area codes vary in length but always begin with 0. Example: "(022)40840621".
- Mobile numbers have no parentheses, but have a space in the middle of the number to help readability. The mobile code of a mobile number is its first four digits and they always start with 7, 8 or 9. Example: "93412 66159".
- Telemarketers' numbers have no parentheses or space, but start with the code 140. Example: "1402316533".

</details>


<details open>
<summary> <b>How It Works<b></summary>

To run the code of each problem just navigate to the folder where the files are and type:

    python Task0.py



Below i list some useful Links:
- [BigO Cheat Sheet](https://www.bigocheatsheet.com/)
- [BigO Notation](https://en.wikipedia.org/wiki/Big_O_notation)

</details>


<details open>
<summary> <b>Project Set Up and Installation<b></summary>

- Download Anaconda
- Install Anaconda
- Create a virtual environment *conda create -n dsa python=3.6*
- Activate the environment *conda activate dsa*
- Install some usefull dependencies *pip install _dependencies_*
- You are ready to go!

</details>

<details open>
<summary> <b>Files and Folders<b></summary>

- **code**: contains the python scripts and datasets to access.
  - *Task0.py*
  - *Task1.py*
  - *Task2.py*
  - *Task3.py*
  - *Task4.py*
  - *texts.csv*
  - *calls.csv*
  - *text_analysis.txt*
- **README.md**: This file, explanation of the project

</details>

<details open>
<summary> <b>Tasks BigO Analysis <b></summary>

- **Task0**: This task open two lists, each one can be defined as O(1) so the worst case scenario time complexity will be O(1).
- **Task1**: This task has two inputs, *data* and *phone_numbers_buffer*, the worst case of this could be O(n.m), but because the numbers are limited and data is unlimited as input the worst case scenario is O(n^2).
- **Task2**: We can see that we have O(n) for calls, list and others part of the code are just O(1) so for the given input we have the worst case scenario as O(n).
- **Task3**: Here we have calls in the for loop representing O(n) and looking for some numbers in accessing the list, so we have this with O(1). Also, sorting strategies takes  O(n log n). so the  worst case scenario is given by this as  O(n log n).
- **Task4**: The worst-case scenario for this code is determined by the sorted function. The time complexity of other operations (reading files, checking conditions, and appending to lists) is relatively minor compared to the loop over 'calls' and sorting, for the worst case, sorting is  O(n log n).

<details open>
<summary> <b>Contributing<b></summary>

Your contributions are always welcome! Please feel free to fork and modify the content but remember to finally do a pull request.

</details>

<details open>
<summary> :iphone: <b>Having Problems?<b></summary>

<p align = "center">

[<img src="https://img.shields.io/badge/linkedin-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white" />](https://www.linkedin.com/in/riawa)
[<img src="https://img.shields.io/badge/telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white"/>](https://t.me/issaiass)
[<img src="https://img.shields.io/badge/instagram-%23E4405F.svg?&style=for-the-badge&logo=instagram&logoColor=white">](https://www.instagram.com/daqsyspty/)
[<img src="https://img.shields.io/badge/twitter-%231DA1F2.svg?&style=for-the-badge&logo=twitter&logoColor=white" />](https://twitter.com/daqsyspty) 
[<img src ="https://img.shields.io/badge/facebook-%233b5998.svg?&style=for-the-badge&logo=facebook&logoColor=white%22">](https://www.facebook.com/daqsyspty)
[<img src="https://img.shields.io/badge/linkedin-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white" />](https://www.linkedin.com/in/riawe)
[<img src="https://img.shields.io/badge/tiktok-%23000000.svg?&style=for-the-badge&logo=tiktok&logoColor=white" />](https://www.linkedin.com/in/riawe)
[<img src="https://img.shields.io/badge/whatsapp-%23075e54.svg?&style=for-the-badge&logo=whatsapp&logoColor=white" />](https://wa.me/50766168542?text=Hello%20Rangel)
[<img src="https://img.shields.io/badge/hotmail-%23ffbb00.svg?&style=for-the-badge&logo=hotmail&logoColor=white" />](mailto:issaiass@hotmail.com)
[<img src="https://img.shields.io/badge/gmail-%23D14836.svg?&style=for-the-badge&logo=gmail&logoColor=white" />](mailto:riawalles@gmail.com)

</p>

</details>

<details open>
<summary> <b>License<b></summary>
<p align = "center">
<img src= "https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/by-sa.svg" />
</p>
</details>