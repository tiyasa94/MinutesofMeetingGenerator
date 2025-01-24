import React, {useState} from 'react'; 
import FileUpload from './components/FileUpload/FileUpload'; 
import "./App.scss"; 
import AppHeader from './components/AppHeader';



function App() { 
  
  const [isSideNavExpanded,setNav] = useState(false);

  
  return ( 
    <div className="App"> 
      <AppHeader isSideNavExpanded = {isSideNavExpanded} setNav={setNav} />    
      <h1>Minutes of Meeting Generator</h1> 
      <FileUpload /> 
    </div> 
  ); 
} 

export default App;


