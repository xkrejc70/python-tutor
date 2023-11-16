import axios from 'axios';

import React, { Fragment, Component } from 'react';

import Sidebar from "./components/Sidebar";
import Evaluation from "./pages/Evaluation";
import Home from "./pages/Home";
import NoPage from "./pages/NoPage";

import "./components/Sidebar.css";

import { BrowserRouter, Routes, Route } from 'react-router-dom';

function App() {
  return (

	<BrowserRouter>
		<Routes>
			<Route index element={<Home />}></Route>
			<Route path="/home" element={<Home />}></Route>
			<Route path="/evaluation" element={<Evaluation />}></Route>
			<Route path="*" element={<NoPage />}></Route>
		</Routes>
	</BrowserRouter>

    // <Fragment>
    //   <Sidebar/>
    // </Fragment>
  );
}

/*

import { Sidebar, Menu, MenuItem, SubMenu } from 'react-pro-sidebar';

import { RiPencilLine } from "react-icons/ri";

class App extends Component {


	render() {

		return (

			<Sidebar>
				<Menu>
					<SubMenu label="Charts">
					<MenuItem> Pie charts </MenuItem>
					<MenuItem> Line charts </MenuItem>
					</SubMenu>
					<MenuItem> Documentation </MenuItem>
					<MenuItem icon={<RiPencilLine />}>Author</MenuItem>
					<MenuItem> Calendar </MenuItem>
				</Menu>
			</Sidebar>
		)
	}
}


/* Upload button

class App extends Component {

	state = {

		// Initially, no file is selected
		selectedFile: null
	};

	// On file select (from the pop up)
	onFileChange = event => {

		// Update the state
		this.setState({ selectedFile: event.target.files[0] });

	};

	// On file upload (click the upload button)
	onFileUpload = () => {

		// Create an object of formData
		const formData = new FormData();

    // TODO: check if is selected

		// Update the formData object
		formData.append(
			"file",
			this.state.selectedFile,
			this.state.selectedFile.name
		);

		// Details of the uploaded file
		console.log(this.state.selectedFile);

		// Request made to the backend api
		// Send formData object
		axios.post("/api/upload", formData);
	};

	// File content to be displayed after
	// file upload is complete
	fileData = () => {

		if (this.state.selectedFile) {

			return (
				<div>
					<h2>File Details:</h2>
					<p>File Name: {this.state.selectedFile.name}</p>

					<p>File Type: {this.state.selectedFile.type}</p>

				</div>
			);
		} else {
			return (
				<div>
					<br />
					<h4>Choose before Pressing the Upload button</h4>
				</div>
			);
		}
	};

	render() {

		return (
			<div>
				<h3>
					File Upload using React!
				</h3>
				<div>
					<input type="file" onChange={this.onFileChange} />
					<button onClick={this.onFileUpload}>
						Upload!
					</button>
				</div>
				{this.fileData()}
			</div>
		);
	}
}
*/

export default App;
