
import os

file_path = 'testing.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Block 1: Event Listener
search_block_1 = """var contentClosing = document.querySelectorAll(".contbox-top")
contentClosing.forEach(function(el){
        el.addEventListener("click",() =>{
                var son = el.querySelector(".contbox-close")
                var dad = el.closest(".sub-page-pre");
                var box = dad.querySelector(".contbox-content");
                if(box.classList.contains("closed")){
                        box.classList.remove("closed")
                        son.classList.remove("closed")
                }else{
                        box.classList.add("closed")
                        son.classList.add("closed")
                }

        })
})"""

replace_block_1 = """var contentClosing = document.querySelectorAll(".contbox-top")
contentClosing.forEach(function(el){
        el.addEventListener("click",() =>{
                var son = el.querySelector(".contbox-close")
                var dad = el.closest(".sub-page-pre");
                var box = dad.querySelector(".contbox-content");
                if(box.classList.contains("closed")){
                        box.classList.remove("closed")
                        son.classList.remove("closed")
                        el.setAttribute('aria-expanded', 'true');
                }else{
                        box.classList.add("closed")
                        son.classList.add("closed")
                        el.setAttribute('aria-expanded', 'false');
                }

        })
})"""

# Block 2: Initialization
search_block_2 = """            // Add specific aria-labels for icon-only buttons
            if (el.classList.contains('close') && !el.hasAttribute('aria-label')) {
                el.setAttribute('aria-label', 'Close details');
            }
            if (el.classList.contains('dispo-icon') && !el.hasAttribute('aria-label')) {
                el.setAttribute('aria-label', 'View decision details');
            }"""

replace_block_2 = """            // Add specific aria-labels for icon-only buttons
            if (el.classList.contains('close') && !el.hasAttribute('aria-label')) {
                el.setAttribute('aria-label', 'Close details');
            }
            if (el.classList.contains('dispo-icon') && !el.hasAttribute('aria-label')) {
                el.setAttribute('aria-label', 'View decision details');
            }

            // Add aria-expanded for collapsible sections
            if (el.classList.contains('contbox-top')) {
                var dad = el.closest(".sub-page-pre");
                if (dad) {
                    var box = dad.querySelector(".contbox-content");
                    if (box && box.classList.contains("closed")) {
                        el.setAttribute('aria-expanded', 'false');
                    } else {
                        el.setAttribute('aria-expanded', 'true');
                    }
                }
            }"""

# Normalizing newlines for search to be robust against CRLF/LF issues
content_normalized = content.replace('\r\n', '\n')
search_block_1_normalized = search_block_1.replace('\r\n', '\n')
search_block_2_normalized = search_block_2.replace('\r\n', '\n')

if search_block_1_normalized in content_normalized and search_block_2_normalized in content_normalized:
    new_content = content_normalized.replace(search_block_1_normalized, replace_block_1)
    new_content = new_content.replace(search_block_2_normalized, replace_block_2)

    # Write back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Successfully patched testing.js")
else:
    print("Could not find exact blocks to replace.")
    if search_block_1_normalized not in content_normalized:
        print("Block 1 not found.")
    if search_block_2_normalized not in content_normalized:
        print("Block 2 not found.")
