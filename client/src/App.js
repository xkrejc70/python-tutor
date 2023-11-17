import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
// pages
import Upload from "pages/Upload";
import Home from "pages/Home";
import NoPage from "pages/NoPage";

function App() {
	return (
		<BrowserRouter>
			<Routes>
				<Route index element={<Home />}></Route>
				<Route path="/home" element={<Home />}></Route>
				<Route path="/upload" element={<Upload />}></Route>
				<Route path="*" element={<NoPage />}></Route>
			</Routes>
		</BrowserRouter>
	);
}

export default App;
