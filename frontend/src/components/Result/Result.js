// import React from 'react'; 
// import { TextArea } from '@carbon/react'; 
// import "./Result.scss"; 

// const Result = (props) => { 
//   let lines = String(props.result) 
  
//   console.log('typeof lines :>> ', typeof lines); 
//   console.log('sample_text :>> ', lines, typeof lines); 
//   console.log("---->","<html>"+lines.split('</style>')[1])
//   if (lines){
//   lines = "<html>"+lines.split('</style>')[1]
//   }
//   // console.log("<-----",lines.split())
 
//   return ( 
   
//     <div className="TextArea">
//       {/* <div className='' dangerouslySetInnerHTML={{__html: lines}}></div>  */}
//       <pre className='output'>{lines+lines+lines}</pre>
//     </div> // response was generated by LLM with the HTML tag and we are changing this to a proper format in the form of bullet points. We are taking care for this using the package "dangerouslySetInnerHTML" 

//   );
// }

// export default Result; 

import React from 'react'; 
import { TextArea } from '@carbon/react'; 
import "./Result.scss"; 

const Result = (props) => { 
  let lines = String(props.result) 
  
  console.log('typeof lines :>> ', typeof lines); 
  console.log('sample_text :>> ', lines, typeof lines); 
  console.log("---->","<html>"+lines.split('</style>')[1])
  // if (lines){
  // lines = "<html>"+lines.split('</style>')[1]
  // }
 
  return ( 
   
    <div className="TextArea" dangerouslySetInnerHTML={{__html: lines}}>
    </div> 

  );
}

export default Result; 
