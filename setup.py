import setuptools as st

st.setup(
    name='daydif',
    version='1.0',
    description='Utility to quickly calculate number of days falling between calender dates',
    url='http://github.com/kerrycobb/daydif',
    author='Kerry A Cobb',
    author_email='cobbkerry@gmail.com',
    license='MIT',
    packages=st.find_packages(),
    entry_points={
        'console_scripts':[
            'daydif=daydif.cli:cli'
        ]
    }
)
