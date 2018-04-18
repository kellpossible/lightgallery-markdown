from setuptools import setup

setup(
    name='lightgallery_caption',
    version='0.1.0',
    author='Luke Frisken',
    author_email='l.frisken@gmail.com',
    description='Markdown extension to wrap images in lightbox/lightgallery with a caption',
    py_modules=['lightgallery_caption'],
    install_requires = ['markdown>=2.5'],
    classifiers=['Topic :: Text Processing :: Markup :: HTML'],
    license='MIT License',
)

