def test_signup_and_unregister_flow(client):
    # Arrange
    activity = "Tennis Club"
    email = "testuser@example.com"

    # Ensure email is not present before test (best-effort cleanup)
    resp = client.get("/activities")
    participants = resp.json()[activity]["participants"]
    if email in participants:
        client.delete(f"/activities/{activity}/participants/{email}")

    # Act: sign up
    resp_signup = client.post(f"/activities/{activity}/signup", params={"email": email})

    # Assert signup
    assert resp_signup.status_code == 200
    assert "Signed up" in resp_signup.json().get("message", "")

    # Act: unregister
    resp_unreg = client.delete(f"/activities/{activity}/participants/{email}")

    # Assert unregister
    assert resp_unreg.status_code == 200
    assert "unregistered" in resp_unreg.json().get("message", "")
