# Food Recognition Web App
#### A web app that takes in users input of a food image and outputs a classification of the image.

## Background

As an avid "eater" (or foodie), I've always loved to travel to different cities and countries and explore different types of cuisines. Eating is by far one of the most exciting things I have done, other than studying data science, so I wanted to combine the two together. This is an ongoing project that I am still working on. At the current stage, I have only trained the model on 105 different Japanese food dishes, which can be found in this [file](food_list/jap_translate.json). I am not Japanese, nor am I an expert at Japanese food. However, it is one of my favorite type of cuisines, which is why I chose this as my starting point. My hope is that users can use the web app easily by uploading an image of a dish and getting an accurate feedback of what the food is (in English). At the moment, it only provides the classification label, but I have plans of providing other details like nutritional facts in the future. I also plan on creating other models with other cuisines so that the web app can serve different types of cuisines.

## Run the web app

There is a version of the web app currently running [here](link).

If you want to run it locally (perhaps with your own model), you can run the following code from the root folder:
```
cd web_app
python app.py
```

## My Process

### Step 1: Data Collection

The first step for this project is to collect and clean the data. To start, I needed to know what types of Japanese food there were, so I went on a site that had 105 popular Japanese dishes and scraped all the names of the dishes there. The script can be found [here](scripts/create_jap_list.py). Running this script would create a .csv file of a list of 105 Japanese foods. Yes, I do understand that there are definitely more than 105 unique Japanese dishes, but I had to start somewhere. Because I will be using an ImageGenerator from Keras so that I could use the `.flow_from_directory()` method to augment my images, I needed my `images` folder structure to look like this:
```
images
├── train
│   ├── Nigiri
│   │   ├── Nigiri_001.jpg
│   │   ├── Nigiri_002.jpg
│   │   └── ...
│   ├── Edamame
│   │   ├── Edamame_001.jpg
│   │   ├── Edamame_002.jpg
│   │   └── ...
│   └── ...    
├── valid
│   ├── Nigiri
│   │   ├── Nigiri_272.jpg
│   │   ├── Nigiri_.428jpg
│   │   └── ...
│   ├── Edamame
│   │   ├── Edamame_154.jpg
│   │   ├── Edamame_221.jpg
│   │   └── ...
│   └── ...          
└── test
    ├── ...                

```

After setting up my folder structure, I ran the [script](scripts/collect_jap_images.py) to download more than 500 images for each food item in my list. To get better quality images, I manually created a translated document in the `food_list` folder so that my search results could be in Japanese. To then split my data into train, valid, and test portions, I created a [script](scripts/setup_image_folder_structure.py) to setup the `images` folder in preparation for my model.

### Step 2: Building and Training the Model

Once I have collected all the data, I built my model. This step could be found in my Jupyter [notebook](notebooks/Japanese Food Classification.ipynb). Because of the way I split my data, I only had around 300+ images per class for training, which isn't a whole lot. To mitigate this problem, I used Keras's ImageDataGenerator for image augmentation. This allowed me to augment the data on the fly and get better training results.

I attempted several models include a base ConvNet model and other transfer learning models. For now, the best model I came down to is to use VGG16 transfer learning as a feature extraction. I fit my model with a RMSProp(lr=0.0002) optimizer first, and then fine-tuned it with a slower SGD optimizer. (Note: I am still working on getting better accuracies).

### Step 3: Inference

With my current best model, I created a flask web application in the `web_app` folder that could be run with the code shown above. If you have another model that you'd like to test out, you can move your model into the `models` folder inside `web_app` and run it there.
