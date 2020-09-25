import axios from "axios";

// axios settings
axios.defaults.baseURL = process.env.VUE_APP_API_ROOT;
axios.defaults.xsrfHeaderName = "X-CSRFToken";
axios.defaults.xsrfCookieName = 'csrftoken';


const api = axios.create({});


export default {
    /* Include additional API calls here */
}
