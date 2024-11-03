CSS (Cascading Style Sheets) is used to style and layout web pages. It controls the color, font, spacing, and overall visual design of HTML elements. Here's a step-by-step introduction to CSS, with examples for each concept.

---

### Step 1: Basic CSS Syntax

CSS has a simple syntax. Styles are defined using selectors, properties, and values.

Example:

```css
selector {
  property: value;
}
```

Example CSS rule:

```css
h1 {
  color: blue;
  font-size: 24px;
}
```

* `h1` is the selector, targeting all `<h1>` elements.
* `color` and `font-size` are properties, and `blue` and `24px` are their values.

---

### Step 2: Adding CSS to an HTML Document

There are three ways to add CSS to HTML:

1. **Inline CSS**: Adding `style` attribute directly to HTML elements.
   ```html
   <h1 style="color: blue;">Hello, World!</h1>
   ```

2. **Internal CSS**: Using the `<style>` tag inside the `<head>` section.
   ```html
   <head>
     <style>
       h1 {
         color: blue;
       }
     </style>
   </head>
   ```

3. **External CSS**: Creating a separate `.css` file and linking it with the `<link>` tag.
   ```html
   <head>
     <link rel="stylesheet" href="styles.css">
   </head>
   ```
   **In `styles.css`**:
   ```css
   h1 {
     color: blue;
   }
   ```

External CSS is preferred for larger projects because it keeps HTML clean and separates content from styling.

---

### Step 3: Styling Text

CSS can style text properties like color, font size, alignment, and more.

Example:

```css
h1 {
  color: darkgreen;
  text-align: center;
  font-family: Arial, sans-serif;
}

p {
  font-size: 16px;
  line-height: 1.5;
  color: gray;
}
```

Explanation:
- `color`: Sets text color.
- `text-align`: Aligns text (e.g., `center`, `left`, `right`).
- `font-family`: Specifies the font.
- `font-size`: Changes text size.
- `line-height`: Sets spacing between lines.

---

### Step 4: Adding Backgrounds and Borders

CSS can add backgrounds and borders to elements.

Example:

```css
body {
  background-color: #f0f0f0;
}

div {
  background-color: lightblue;
  border: 2px solid blue;
  padding: 10px;
  margin: 15px;
}
```

Explanation:
- `background-color`: Sets the background color.
- `border`: Defines the border’s width, style, and color.
- `padding`: Adds space inside the element.
- `margin`: Adds space outside the element.

---

### Step 5: Styling Lists

You can control how lists look with CSS.

Example:

```css
ul {
  list-style-type: square;
}

li {
  color: darkred;
  font-weight: bold;
}
```

Explanation:
- `list-style-type`: Changes the bullet style (`disc`, `circle`, `square`, or `none`).
- `font-weight`: Controls boldness (`normal`, `bold`).

---

### Step 6: Layout with Flexbox

CSS Flexbox is a powerful layout tool that aligns elements in rows or columns.

Example:

```css
.container {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.item {
  padding: 10px;
  background-color: lightcoral;
}
```

Explanation:
- `display: flex`: Makes the container a flex container.
- `justify-content`: Aligns items horizontally.
- `align-items`: Aligns items vertically.

---

### Step 7: CSS Grid for Advanced Layout

CSS Grid is useful for creating complex layouts with rows and columns.

Example:

```css
.grid-container {
  display: grid;
  grid-template-columns: auto auto auto;
  gap: 10px;
}

.grid-item {
  background-color: lightgreen;
  padding: 20px;
  text-align: center;
}
```

Explanation:
- `display: grid`: Turns the container into a grid.
- `grid-template-columns`: Defines the number and size of columns.
- `gap`: Sets spacing between grid items.

---

### Step 8: Hover Effects and Transitions

CSS allows interactive styling, such as changing color on hover.

Example:

```css
button {
  background-color: orange;
  color: white;
  padding: 10px 20px;
  border: none;
  cursor: pointer;
  transition: background-color 0.3s;
}

button:hover {
  background-color: darkorange;
}
```

Explanation:
- `transition`: Controls the speed of property changes (in this case, `background-color`).
- `:hover`: Applies a style when hovering over the element.

---

### Full Example with CSS

Here’s a complete example, including HTML and CSS.

**HTML (index.html):**

```html
<!DOCTYPE html>
<html>
  <head>
    <title>My Styled Page</title>
    <link rel="stylesheet" href="styles.css">
  </head>
  <body>
    <h1>Welcome to My Page</h1>
    <p>This page is styled with CSS!</p>

    <div class="container">
      <div class="item">Item 1</div>
      <div class="item">Item 2</div>
      <div class="item">Item 3</div>
    </div>

    <button>Click Me</button>
  </body>
</html>
```

**CSS (styles.css):**

```css
body {
  background-color: #f4f4f9;
  font-family: Arial, sans-serif;
}

h1 {
  color: #333;
  text-align: center;
  font-size: 36px;
  margin-top: 20px;
}

p {
  text-align: center;
  color: #666;
  font-size: 18px;
}

.container {
  display: flex;
  justify-content: space-around;
  margin: 20px;
}

.item {
  background-color: #85c1e9;
  color: white;
  padding: 20px;
  border-radius: 8px;
  text-align: center;
}

button {
  display: block;
  margin: 20px auto;
  padding: 10px 20px;
  background-color: #e67e22;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s;
}

button:hover {
  background-color: #d35400;
}
```

This example uses various CSS techniques to style the HTML elements, creating a simple and visually appealing webpage.