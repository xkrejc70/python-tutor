import React, { useState, useEffect } from 'react';
import 'assets/global.css';

function Quiz({ updateCode }) {
  const [questions, setQuestions] = useState([]);
  const [currentQuestion, setCurrentQuestion] = useState(0);
  const [selectedOption, setSelectedOption] = useState(null);
  const [showResult, setShowResult] = useState(false);
  const [showContinue, setShowContinue] = useState(false);

  useEffect(() => {
    // Fetch questions from the API when the component mounts
    fetch('http://localhost:5005/api/questions/proj8')
      .then(response => response.json())
      .then(data => setQuestions(data))
      .catch(error => console.error('Error fetching questions:', error));
  }, []);

  const handleOptionSelect = (index) => {
    setSelectedOption(index);
    setShowResult(true);
    
    if (index === correctOption) {
      setShowContinue(true);
      updateCode(currentQuestion);
    }
  };

  const handleNextQuestion = () => {
    setSelectedOption(null);
    setShowResult(false);
    setShowContinue(false);

    if (currentQuestion < questions.length - 1) {
      setCurrentQuestion((prev) => prev + 1);
    } else {
      console.log('Quiz completed!');
    }
  };

  if (questions.length === 0) {
    // Loading state while fetching questions
    return <div>Loading Quiz...</div>;
  }

  const { question, options, correctOption, explanations } = questions[currentQuestion];

  return (
    <div className="quiz-container">
      <div className="question">{question}</div>
      <div className="options-container">
        {options.map((option, index) => (
          <div
            key={index}
            className={`option ${selectedOption === index ? 'selected' : ''}`}
            onClick={() => handleOptionSelect(index)}
          >
            {option}
          </div>
        ))}
      </div>
      {showResult && (
        <div className={`result ${selectedOption === correctOption ? 'success' : 'failure'}`}>
          {selectedOption === correctOption ? (
            <>
              <h2 className='heading-h2'>Correct!</h2>
              <p>{explanations[selectedOption]}</p>
            </>
          ) : (
            <>
              <h2 className='heading-h2'>Incorrect! Try again.</h2>
              <p>{explanations[selectedOption]}</p>
            </>
          )}
        </div>
      )}
      {showResult && showContinue && (
        currentQuestion < questions.length - 1 &&
        <button onClick={handleNextQuestion} className="next-button d-block mr-0 ml-auto">
          Continue
        </button>
      )}
    </div>
  );
}

export default Quiz;