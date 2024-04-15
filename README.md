# Movie Genre Classification

The aim of this project is to classify movie genres. As an input the model will get the movie description. This project uses the IMDB Movies Dataset from Hugging Face

https://huggingface.co/datasets/adrienheymans/imdb-movie-genres

# How to use

To use this small model you have to navigate into the frontend folder. Afterwards, you have to install the npm packages and then run the development setup
```
cd frontend
npm install
npm run dev
```

The BERT model is running on hugging face. The backend is containerized with Docker and pushed to Microsoft Azure Therefore, it is not needed to install anything anymore.
After running npm run dev, vite will create a Vue.js app on your localhost.


# Tools & Frameworks

Below is a list of Tools and Frameworks that were used.

- Vue.js
- FastAPI
- "uvicorn[standard]"
- Transformers
- PyTorch
- Docker
- Microsoft Azure
- Hugging Face
- GitHub

