import numpy as np
# %%


def find_dog(path):
    import cv2
    import tensorflow as tf

    def prepare(path):
        img_array = cv2.imread(path, cv2.IMREAD_COLOR)
        img_array = img_array/255
        new_array = cv2.resize(img_array, (331, 331))
        return new_array.reshape(-1, 331, 331, 3)
    model = tf.keras.models.load_model("history")

    list = ['affenpinscher', 'afghan_hound', 'african_hunting_dog', 'airedale', 'american_staffordshire_terrier', 'appenzeller', 'australian_terrier', 'basenji', 'basset', 'beagle', 'bedlington_terrier', 'bernese_mountain_dog', 'black-and-tan_coonhound', 'blenheim_spaniel', 'bloodhound', 'bluetick', 'border_collie', 'border_terrier', 'borzoi', 'boston_bull', 'bouvier_des_flandres', 'boxer', 'brabancon_griffon', 'briard', 'brittany_spaniel', 'bull_mastiff', 'cairn', 'cardigan', 'chesapeake_bay_retriever', 'chihuahua', 'chow', 'clumber', 'cocker_spaniel', 'collie', 'curly-coated_retriever', 'dandie_dinmont', 'dhole', 'dingo', 'doberman', 'english_foxhound', 'english_setter', 'english_springer', 'entlebucher', 'eskimo_dog', 'flat-coated_retriever', 'french_bulldog', 'german_shepherd', 'german_short-haired_pointer', 'giant_schnauzer', 'golden_retriever', 'gordon_setter', 'great_dane', 'great_pyrenees', 'greater_swiss_mountain_dog', 'groenendael', 'ibizan_hound', 'irish_setter', 'irish_terrier', 'irish_water_spaniel', 'irish_wolfhound',
            'italian_greyhound', 'japanese_spaniel', 'keeshond', 'kelpie', 'kerry_blue_terrier', 'komondor', 'kuvasz', 'labrador_retriever', 'lakeland_terrier', 'leonberg', 'lhasa', 'malamute', 'malinois', 'maltese_dog', 'mexican_hairless', 'miniature_pinscher', 'miniature_poodle', 'miniature_schnauzer', 'newfoundland', 'norfolk_terrier', 'norwegian_elkhound', 'norwich_terrier', 'old_english_sheepdog', 'otterhound', 'papillon', 'pekinese', 'pembroke', 'pomeranian', 'pug', 'redbone', 'rhodesian_ridgeback', 'rottweiler', 'saint_bernard', 'saluki', 'samoyed', 'schipperke', 'scotch_terrier', 'scottish_deerhound', 'sealyham_terrier', 'shetland_sheepdog', 'shih-tzu', 'siberian_husky', 'silky_terrier', 'soft-coated_wheaten_terrier', 'staffordshire_bullterrier', 'standard_poodle', 'standard_schnauzer', 'sussex_spaniel', 'tibetan_mastiff', 'tibetan_terrier', 'toy_poodle', 'toy_terrier', 'vizsla', 'walker_hound', 'weimaraner', 'welsh_springer_spaniel', 'west_highland_white_terrier', 'whippet', 'wire-haired_fox_terrier', 'yorkshire_terrier']

    life_span = {"affenpinscher": "12-14 years",
                 "afghan_hound": "12-14 years",
                 "african_hunting_dog": "5-7 years",
                 "airedale": "10-12 years",
                 "american_staffordshire_terrier": "12-16 years",
                 "appenzeller": "12-14 years",
                 "australian_terrier": "12-15 years",
                 "basenji": "12-16 years",
                 "basset": "10-12 years",
                 "beagle": "12-15 years",
                 "bedlington_terrier": "12-14 years",
                 "bernese_mountain_dog": "6-8 years",
                 "black-and-tan_coonhound": "10-12 years",
                 "blenheim_spaniel": "12-14 years",
                 "bloodhound": "10-12 years",
                 "bluetick": "11-12 years",
                 "border_collie": "10-17 years",
                 "border_terrier": "12-15 years",
                 "borzoi": "7-10 years",
                 "boston_bull": "13-15 years",
                 "bouvier_des_flandres": "10-12 years",
                 "boxer": "10-12 years",
                 "brabancon_griffon": "10-15 years",
                 "briard": "10-12 years",
                 "brittany_spaniel": "12-15 years",
                 "bull_mastiff": "8-10 years",
                 "cairn": "12-15 years",
                 "cardigan": "12-15 years",
                 "chesapeake_bay_retriever": "10–12 years",
                 "chihuahua": "12-18 years",
                 "chow": "12-16 years",
                 "clumber": "10–12 years",
                 "cocker_spaniel": "12-15 years",
                 "collie": "10-14 years",
                 "curly-coated_retriever": "9-14 years",
                 "dandie_dinmont": "12-14 years",
                 "dhole": "10-13 years",
                 "dingo": "8-10 years",
                 "doberman": "10-13 years",
                 "english_foxhound": "10-13 years",
                 "english_setter": "10-12 years",
                 "english_springer": "12-14 years",
                 "entlebucher": "11-15 years",
                 "eskimo_dog": "13-15 years",
                 "flat-coated_retriever": "8-14 years",
                 "french_bulldog": "10-14 years",
                 "german_shepherd": "9-13 years",
                 "german_short-haired_pointer": "12-14 years",
                 "giant_schnauzer": "12-15 years",
                 "golden_retriever": "10-12 years",
                 "gordon_setter": "10-12 years",
                 "great_dane": "8-10 years",
                 "great_pyrenees": "10-12 years",
                 "greater_swiss_mountain_dog": "10-11 years",
                 "groenendael": "13-14 years",
                 "ibizan_hound": "10-12 years",
                 "irish_setter": "12-15 years",
                 "irish_terrier": "13-15 years",
                 "irish_water_spaniel": "10-12 years",
                 "irish_wolfhound": "6-10 years",
                 "italian_greyhound": "12-15 years",
                 "japanese_spaniel": "12-14 years",
                 "keeshond": "13–15 years",
                 "kelpie": "15-16 years",
                 "kerry_blue_terrier": "12-15 years",
                 "komondor": "10–12 years",
                 "kuvasz": "10–12 years",
                 "labrador_retriever": "10-12 years",
                 "lakeland_terrier": "12-16 years",
                 "leonberg": "8-9 years",
                 "lhasa": "12–14 years",
                 "malamute": "10–12 years",
                 "malinois": "10–14 years",
                 "maltese_dog": "12–15 years",
                 "mexican_hairless": "12–15 years",
                 "miniature_pinscher": "13-15 years",
                 "miniature_poodle": "12-14 years",
                 "miniature_schnauzer": "12-15 years",
                 "newfoundland": "8-10 years",
                 "norfolk_terrier": "12-15 years",
                 "norwegian_elkhound": "12–15 years",
                 "norwich_terrier": "12-14 years",
                 "old_english_sheepdog": "12-15 years",
                 "otterhound": "13–15 years",
                 "papillon": "13-15 years",
                 "pekinese": "12-15 years",
                 "pembroke": "12-15 years",
                 "pomeranian": "12-16 years",
                 "pug": "12-15 years",
                 "redbone": "11-12 years",
                 "rhodesian_ridgeback": "12-14 years",
                 "rottweiler": "8-10 years",
                 "saint_bernard": "10-12 years",
                 "saluki": "12-14 years",
                 "samoyed": "12-15 years",
                 "schipperke": "12-15 years",
                 "scotch_terrier": "12–15 years",
                 "scottish_deerhound": "8-11 years",
                 "sealyham_terrier": "13–15 years",
                 "shetland_sheepdog": "10-12 years",
                 "shih-tzu": "10-16 years",
                 "siberian_husky": "12-15 years",
                 "silky_terrier": "12-15 years",
                 "soft-coated_wheaten_terrier": "12-15 years",
                 "staffordshire_bullterrier": "12-14 years",
                 "standard_poodle": "12-15 years",
                 "standard_schnauzer": "12-15 years",
                 "sussex_spaniel": "12–15 years",
                 "tibetan_mastiff": "12-14 years",
                 "tibetan_terrier": "13–15 years",
                 "toypoodle": "12–15 years",
                 "toy_terrier": "10-12 years",
                 "vizsla": "12–15 years",
                 "walker_hound": "12-14 years",
                 "weimaraner": "11-14 years",
                 "welsh_springer_spaniel": "13–15 years",
                 "west_highland_white_terrier": "12-14 years",
                 "whippet": "12-15 years",
                 "wire-haired_fox_terrier": "10-12 years",
                 "yorkshire_terrier": "12-15 years"}

    prediction = model.predict([prepare(path)])
    a = np.argmax(prediction)
    dog_breed = list[a]
    dog_span = life_span[dog_breed]
    #print("Breed: "+dog_breed)
    #print("Life Span: "+dog_span)
    return dog_breed, dog_span


# %%
