import React, { useState } from 'react';
import {
  FileUploaderDropContainer,
} from '@carbon/react';
import "./FileUpload.scss";
import "../Result/Result"
import Result from '../Result/Result';


function FileUpload() {
  const [got_response, setgot_response] = useState(false)
  const [result, setResult] = useState('');

  const handleFileUpload = async (event) => {
    const file = event.target.files[0];
    
    if (file) {
      const formData = new FormData();
      formData.append('file', file);
      console.log("Sending API request")
      try {
        const response = await fetch('http://127.0.0.1:8000/file', {
          method: 'POST',
          body: formData,
        });

        if (response.ok) {
          setgot_response (true)
          console.log('response :>> ', response);
          const resultString = await response.text();
          const length = await resultString.length; // Add this line
          console.log("Result String:", resultString.substring(1,length-1));
          // result.replace(/\n/g, '<br>');
          await setResult(resultString.substring(1,length-1));
          
        } else {
          console.error('Server error:', response);
          console.log(await response.text()); // Log server error response
        }
       
      } catch (error) {
        console.error('Upload failed:', error);
      }
    }
  };

  return (
    <div className='Flex'>
          <div className='Component1'>
              <FileUploaderDropContainer  
              labelText="Upload Webex transcript (.txt) here" multiple={false} accept={[".txt"]} disabled={false} onAddFiles={handleFileUpload} filenamestatus='complete'  />
          </div>
          <div className='Component2' >
             {got_response && <Result result = {result}/>}
            
          </div>
        
    </div>

  );
}

export default FileUpload;
margin-bottom: 0.5rem;
    font-weight: 400;
    margin-left: 1.5rem;
    list-style:disc outside none;
    display:list-item; 