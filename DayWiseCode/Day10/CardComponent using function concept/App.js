import './App.css';
import Card from './componenet.js';

function App() {
  return (
    <div className="App">
      <h1>Hello</h1>
      <Card image="https://placehold.co/100x100" title="Ear Phones" price="123" rating="⭐⭐⭐⭐☆"/>  
      <Card image="https://placehold.co/100x100" title="Head" price="99" rating="⭐⭐⭐⭐☆"/>  
      <Card image="https://placehold.co/100x100" title="Buds " price="199" rating="⭐⭐⭐⭐☆"/>  
      <Card image="https://placehold.co/100x100" title="Iphone" price="299" rating="⭐⭐⭐⭐☆"/>  
      <Card image="https://placehold.co/100x100" title="ANdriod" price="399" rating="⭐⭐⭐⭐☆"/>  
      <Card image="https://placehold.co/100x100" title="Computer" price="499" rating="⭐⭐⭐⭐☆"/>  
     </div>
  );
}

export default App;
