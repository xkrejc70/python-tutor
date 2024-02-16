import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
// font
import "@fontsource/montserrat";
import '@fontsource-variable/source-code-pro';

// css
import 'assets/global.css';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
