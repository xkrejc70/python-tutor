import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import PrivateRoute from 'PrivateRoute';
// pages
import Upload from "pages/upload/Upload";
import About from "pages/about/About";
import Settings from "pages/settings/Settings";
import Login from "pages/login/Login";
import Proj8 from "pages/exercise/Proj8";
import Proj4 from "pages/exercise/Proj4";
import NoPage from "pages/page404/NoPage";
import Evaluation from "pages/evaluation/Evaluation";

function App() {
	return (
		<BrowserRouter>
			<Routes>
				<Route index element={<Upload />}></Route>
				<Route path="/settings" element={
					<PrivateRoute>
						<Settings />
					</PrivateRoute>} />
				<Route path="/login" element={<Login />}></Route>
				<Route path="/upload" element={<Upload />}></Route>
				<Route path="/about" element={<About />}></Route>
				<Route path="/evaluation" element={<Evaluation />}></Route>
				<Route path="/proj8" element={<Proj8 />}></Route>
				<Route path="/proj4" element={<Proj4 />}></Route>
				<Route path="*" element={<NoPage />}></Route>
			</Routes>
		</BrowserRouter>
	);
}

export default App;
