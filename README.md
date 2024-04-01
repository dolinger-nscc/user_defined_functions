<div align="center">
	<br>
		<img src="img/header.svg" width="800" height="400">
	<br>
</div>
<br>
<div>
	<h1><img src="img/question.png" width="40" /> How do I access my GitHub UDFs?<img src="img/bulb.png" width="40" /></h1>
</div>
<br>
You cannot import a model file (.py file) directly from GitHub into your Jupyter Notebook. Jupyter Notebooks also require the module with your user defined functions to be in the same directory as your notebook file (.ipynb file). The easiest way to work around this and ensure you have the latest version of your udf.py (name used for this exercise) is to download it each time you require the functions in your notebook. The following block of code copy down your udf.py file to the same directory as the notebook that is calling it. As long as you keep your udf.py updated in GitHub, you will get the most current copy each time as the file will overwrite any prior udf.py in the directory.  
<br><br>
<strong>Note:</strong> Currently this block of code will copy down <strong>my</strong> udf.py file.
<br>Edit the url to point to yours. 

```python
import requests

url = 'https://raw.githubusercontent.com/dolinger-nscc/user_defined_functions/main/udf.py' 
response = requests.get(url)

with open('udf.py', 'w') as file:
    file.write(response.text)
response.close()

import udf
```


  
Right click on the video preview and select "Open link in new tab"  
[<img src="https://img.youtube.com/vi/48OBj6DtYSk/hqdefault.jpg" width="600"  /> ](https://www.youtube.com/embed/48OBj6DtYSk)


<div>
	<h1><img src="img/question.png" width="40" /> How do I reuse common code snippets?</h1>
</div>
<br>
The remainder of this repository illustrates the use of a .py file as a module for reusable code. This method was designed primarily for use with Jupyter Notebooks. Its design intent is to help students new to Data Science concepts practice their Python skills as well to implement consistent data wrangling within their workflows. The repository will consist of code snippets that utilize the udf.py file included.  

Each function within the udf.py file will be explained below:  
<div>
	<h2><img src="img/bulb.png" width="40" /> Creating a "set-aside" dataset</h2>
</div>
<br>
You will often want to create a "set-aside" dataset to be used after creating your model. This is a good final step as this data will not have been exposed to the algorithm during the training process. This will reduce the chance of data leakage occuring prior to your final scoring of the model.  
<br>


  
Right click on the video preview and select "Open link in new tab"  
[<img src="https://img.youtube.com/vi/lVTObDXu4QM/hqdefault.jpg" width="600"  /> ](https://www.youtube.com/embed/lVTObDXu4QM)


<br>
<br>
The header file was created as a hack of this <a href="https://css-tricks.com/custom-styles-in-github-readmes/" target="_blank"><i>Custom Styles in Github Readme Files</i></a> article on css-tricks.com.  

The data used for this demonstrations are thanks to Allison Horst and her <a href="https://allisonhorst.github.io/palmerpenguins/" target="_blank"><i>Palmer Penguins Dataset</i></a>. 

