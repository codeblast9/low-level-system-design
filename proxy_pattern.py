'''# Proxy Pattern Benefits

Lazy Loading: The real object is created and loaded only when you actually need it, which saves memory and speeds up your application startup time.

Access Control: The proxy can check permissions and control who gets to access the real object – like a security guard checking IDs before letting people enter.

Adding Extra Features: Proxies can add useful features like logging (tracking who accessed what), caching (storing results for faster access), or validation, all without changing the original object's code.

Keeping Things Organized: The real object focuses only on its main job (like displaying images), while the proxy handles all the extra stuff like loading, security checks, and caching. This keeps the code clean and organized.'''


import time
from typing import List

class HighResolutionImage:
    def __init__(self,file_name:str):
        self.__file_name = file_name
        self.__image_data = None

        self.load_from_disk()


    def load_from_disk(self):
        time.sleep(2)
        self.__image_data =f"{self.__file_name}"
        print(f"loaded the {self.__image_data} from the disk")

    def display(self):
        print(f"{self.__file_name} has data of image {self.__image_data}")

class ImageProxy:
    def __init__(self,file_name:str):
        self.__file_name = file_name
        self.__real_image = None

    def display(self):
        if self.__real_image is None:
            self.__real_image = HighResolutionImage(self.__file_name)
        self.__real_image.display()
        


class PhotoGallery:
    def __init__(self):
        self.__images:list[ImageProxy] = []

    def add_image(self,file_name:str):
        high_res_image = ImageProxy(file_name)
        self.__images.append(high_res_image)

    def display_gallery(self):
        for image in self.__images:
            image.display()

    def display_image(self,index:int):
        self.__images[index - 1].display()



start = time.time()
photogallery = PhotoGallery()
photogallery.add_image("image1.png")
photogallery.add_image("image2.png")
photogallery.add_image("image3.png")
photogallery.add_image("image4.png")
end = time.time()
print(f"{end - start:.2f}")

photogallery.display_image(2)
