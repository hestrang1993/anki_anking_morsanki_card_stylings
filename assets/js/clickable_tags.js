                        var tagContainer = document.getElementById("tags-container");
                        if (tagContainer.childElementCount == 0) {
                            var tagList = tagContainer.innerHTML.split(" ");
                            var kbdList = [];
                            var newTagContent = document.createElement("div");

                            for (var i = 0; i < tagList.length; i++) {
                                var newTag = document.createElement("kbd");
                                newTag.innerHTML = tagList[i];
                                newTagContent.append(newTag);
                            }
                            tagContainer.innerHTML = newTagContent.innerHTML;
                            tagContainer.style.cursor = "default";
                        }