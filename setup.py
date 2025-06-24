from setuptools import setup, find_packages

setup(
    name='dynamicreasoning',
    version='0.1.0',
    packages=find_packages(include=['dynamicreasoning', 'dynamic_agent', 'ui']),
    py_modules=['metrics', 'static_agent', 'enhanced_agents', 'web_api', 'web_server'],
    entry_points={
        'console_scripts': [
            'dynamicreasoning=dynamicreasoning.cli:main',
        ]
    },
    python_requires='>=3.8',
)
