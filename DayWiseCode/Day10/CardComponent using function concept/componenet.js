
function Card(props){
    return <>
         <div class="card">
            <img src={props.image} alt="ProductImage" />
            <h2>{props.title}</h2>
            <p class="price">${props.price}</p>
            <p class="rating">{props.rating}</p>
            {/* ⭐⭐⭐⭐☆ */}
            <button>Add to Cart</button>
    </div>
    </>
}

// Card(name = "rakesh",price= 34)
export default Card;

