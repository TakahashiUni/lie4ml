import axios from "axios";

const API_URL = "http://localhost:8000/api/v1/articles";

export const getArticles = async () => {
  const response = await axios.get(`${API_URL}`);
  return response.data;
};
