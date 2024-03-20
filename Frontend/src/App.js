import React from 'react';
import './App.css';
import FileUpload from './components/FileUpload';
import QueryForm from './components/QueryForm';

function App() {
    return (
        <div className="App">
            <h1>Chatbot Application</h1>
            <FileUpload />
            <QueryForm />
        </div>
    );
}

export default App;
