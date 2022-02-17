setup(
    name="text_to_audio",
    version="1.0.0",
    description="convert text to audio file",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/OMRYZUTA/text_to_audio",
    author="Omry Zuta",
    author_email="omryzuta@gmail.com",
    license="Apache License 2.0",
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    packages=["text_to_audio"],
    include_package_data=True,
    install_requires=[
        "tkinter", "Gtts"
    ],
    entry_points={"console_scripts": ["OmryZuta=src.ui.main:main"]},
)