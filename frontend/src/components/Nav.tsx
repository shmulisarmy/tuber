<a style={{ float: "right" }} href="/logout">
  Logout
</a>;
export default function Nav() {
  return (
    <nav
        style={{
          position: "fixed",
          top: 0,
          left: 0,
          width: "100%",
          display: "flex",
          gap: "20px",
          "justify-content": "space-around",
          "align-items": "center",
          padding: "10px",
          background: "var(--background-color)",
          "box-shadow": "0 2px 4px rgba(0, 0, 0, 0.1)",
          "border-bottom": "2px solid var(--border-color)",
          "z-index": 999,
        }}
    >
          <img
        width={"30px"}
        style={{ "border-radius": "50%" }}
        src="data:image/jpeg;base64,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"
        alt=""
      />
      <svg aria-hidden="true" aria-label="" class="BNH gUZ U9O kVc" height="24" role="img" viewBox="0 0 24 24" width="24"><path d="M19 7v6.17A10 10 0 0 1 22 19H2a10 10 0 0 1 3-5.83V7a7 7 0 1 1 14 0m-4 14a3 3 0 1 1-6 0z"></path></svg>
      <svg aria-label="Search icon" class="BNH gUZ U9O kVc" height="16" role="img" viewBox="0 0 24 24" width="16"><path d="M10 16a6 6 0 1 1 .01-12.01A6 6 0 0 1 10 16m13.12 2.88-4.26-4.26a10 10 0 1 0-4.24 4.24l4.26 4.26a3 3 0 1 0 4.24-4.24"></path></svg>
   <input style={{
    "margin-left": "20px",
    "border-radius": "20px",
    "box-shadow": "0 2px 4px rgba(0, 0, 0, 0.1)",
   }} type="search" />
      <div
        class="links"
        style={{
          width: "100%",
          display: "flex",
          "justify-content": "space-around",
          "align-items": "center",
        }}
      >
        <a href="/">Home</a>
        <a href="/recipes">Recipes</a>
        <a style={{ float: "right" }} href="/logout">
          Logout
        </a>
  <button onclick={() => document.body.classList.toggle("dark-mode")}>dark mode</button> 

      </div>
    
    </nav>
  );
}
