from setuptools import setup

setup(
    name='django-socialtags',
    version='0.0.1',

    author='James Robert, Ivan Schmidt-Vitale',
    author_email='jiaaro@gmail.com, isvitale@gmail.com',

    description=('Template tags for social media sharing buttons'),
    long_description=open('README.markdown').read(),

    license='MIT',
    keywords='social template tags share buttons',

    #url='',

    install_requires=[
        "django",
    ],

    packages=[
        'socialtags',
    ],

    include_package_data=True,


    classifiers=[
    	'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Framework :: Django',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Utilities'
    ]
)
