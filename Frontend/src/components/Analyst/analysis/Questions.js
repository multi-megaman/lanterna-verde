import React, {useEffect, useState} from 'react';
import './Question.css';
import Collapse from 'react-bootstrap/Collapse';
const Questions = ({ questao, analysis, setDimensions, handleCheckBoxClick, handleSourceChange, handleJustificationChange }) => {
    
    const [active, setActive] = useState(false);
    useEffect(() => {
        // setQuest(questao)
        initAnswer()
    },[])

    function initAnswer(){
        var box = document.getElementById('question'+questao.id)
        if (questao.answer){
            box.style.animation = "positive-neutral 0.125s linear forwards";
        }
        else{
            box.style.animation = "negative-neutral 0.125s linear forwards";
        }
    }
         
    function answerHandler(){
        var box = document.getElementById('question'+questao.id)
        if (questao.answer){
            box.style.animation = "negative 0.125s linear forwards";
            // questao.answer = !questao.answer
            
        }
        else{
            box.style.animation = "positive 0.125s linear forwards";
            // questao.answer = !questao.answer
        }
        handleCheckBoxClick(questao)

    }
      
    function sourceAreaChange() {
        let sourceValue = document.getElementById("questionSource"+questao.id).value
        handleSourceChange(sourceValue,questao)
    }

    function justificationAreaChange() {
        let justificationValue = document.getElementById("questionJustification"+questao.id).value
        handleJustificationChange(justificationValue,questao)
    }

    function questionClickHandler() {
        setActive(!active)
    }

    // document.onload = initAnswer();
    return <>
            <script src="https://unpkg.com/react/umd/react.production.min.js"></script>
            <script src="https://unpkg.com/react-collapse/build/react-collapse.min.js"></script>
            <div className='question-container'>

                {/* <div className='negative-container'> */}
                    <button className='negative-btn' onClick={answerHandler}>
                    <img src="../images/x.svg" alt="X"/>
                    </button>
                {/* </div> */}
                

                <div className='full-question-area'>
                    {/* <div className='question-and-awnser'> */}
                    
                    {/* <UnmountClosed isOpened={active} initialStyle={{height: 0, overflow: 'hidden'}}>
                        alooooooooooooooooooooooooooooooooooo
                    </UnmountClosed> */}


                    {/* <div className='alig-areas'> */}
                        <div className='questionArea' id={'question'+questao.id} onClick= {questionClickHandler}>
                            {questao.question.body} 
                        </div>

                    <Collapse in={active}>
                        <div className='justi-src-container'>
                            <div className='justification-container' >
                                <div className='just-tittle'>Justificativa:</div>
                                <textarea  className='justificationArea' id = {'questionJustification'+questao.id} onChange={justificationAreaChange}>{questao.justification}</textarea>  <br></br>
                            </div>
                            
                            <div className='source-container'>
                                <div className='source-tittle'>Fonte:</div>
                                <textarea  className='sourceArea' id = {'questionSource'+questao.id} onChange={sourceAreaChange}>{questao.source}</textarea> <br></br>
                            </div>
                        </div> 
                    </Collapse>




                    {/* </div> */}

                       
                            {/* <label class="switch">
                                <input type="checkbox" onClickCapture={() => handleCheckBoxClick(questao)} defaultChecked={questao.answer}></input>
                                <span class="slider round">
                                </span>
                            </label>  */}
                    {/* </div> */}
                </div>
                {/* <div className='positive-container'> */}
                    <button className='positive-btn' onClick={answerHandler}>
                        <img src="../images/v.svg" alt="V"/>
                    </button>   
                {/* </div> */}


            </div>
            </>
}; 

export default Questions;