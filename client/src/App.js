import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import PrivateRoute from 'PrivateRoute';
// pages
import Upload from "pages/Upload";
import Admin from "pages/Admin";
import Login from "pages/Login";
import Proj8 from "pages/Proj8";
import Proj4 from "pages/Proj4";
import NoPage from "pages/NoPage";
import Evaluation from "pages/Evaluation";

function App() {
	return (
		<BrowserRouter>
			<Routes>
				<Route index element={<Upload />}></Route>
				<Route path="/admin" element={
					<PrivateRoute>
						<Admin />
					</PrivateRoute>} />
				<Route path="/login" element={<Login />}></Route>
				<Route path="/upload" element={<Upload />}></Route>
				<Route path="/evaluation" element={<Evaluation />}></Route>
				<Route path="/proj8" element={<Proj8 />}></Route>
				<Route path="/proj4" element={<Proj4 />}></Route>
				<Route path="*" element={<NoPage />}></Route>
			</Routes>
		</BrowserRouter>
	);
}

export default App;
